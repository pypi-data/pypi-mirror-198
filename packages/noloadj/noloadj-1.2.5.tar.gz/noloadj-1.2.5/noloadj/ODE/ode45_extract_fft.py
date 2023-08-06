from jax.lax import *
from jax import interpreters
from noloadj.ODE.ode45 import rk_step_der,next_step_simulation
from noloadj.ODE.ode45_fft import odeint45_fft,odeint45_fft_etendu
from noloadj.ODE.ode_tools import *

def odeint45_extract_fft(f,y0,*args,M,T=0.,h0=1e-5,tol=1.48e-8):
    return _odeint45_extract_fft(f,h0,tol,M,y0,T,*args)


@partial(custom_jvp,nondiff_argnums=(0,1,2,3))
def _odeint45_extract_fft(f,h0,tol,M,y0,T,*args):
    type,cond_stop=f.stop

    def cond_fn(state):
        y_prev2,_,y_prev,t_prev,h,cstr,_=state
        return (h > 0) & cond_stop(t_prev,t_prev+h,cstr)

    def body_fn(state):
        _,_,y_prev,t_prev,h,cstr,i=state

        y,t_now,hopt,inew=next_step_simulation(y_prev,t_prev,i,h,f,tol,h0,
                                                   T,*args)

        if f.constraints!={}:
            for i in f.constraints.keys():
                if isinstance(f.constraints[i][1],tuple):
                    test_exp,(_,expression,_,_,_,_)=f.constraints[i]
                else:
                    (_,expression,_,_,_,_)=f.constraints[i]
                    test_exp = lambda t: True
                cstr[i]=np.where(test_exp(t_now),expression(t_prev,
                            y_prev, t_now, y,cstr[i],h,T,f.names),cstr[i])

        return y_prev,t_prev,y,t_now,hopt,cstr,inew

    cstr=dict(zip(list(f.constraints.keys()),[0.]*len(f.constraints)))# INITIALISATION
    freq_cstr=dict(zip(list(f.freq_constraints.keys()),
                                [0.] * len(f.freq_constraints)))
    if f.constraints!={}:
        for i in f.constraints.keys():
            if isinstance(f.constraints[i][1],tuple):
                test_exp,(init,_,_,_,_,_)=f.constraints[i]
            else:
                (init,_,_,_,_,_)=f.constraints[i]
                test_exp=lambda t:True
            cstr[i]=np.where(test_exp(0.),init(y0,0.,h0,f.names),cstr[i])

    if hasattr(f,'etat_actuel'):
        i0=f.etat_actuel
    else:
        i0=0
    _,_,yf,ts,h,cstr,_=while_loop(cond_fn,body_fn,(y0,0.,y0,0.,h0,cstr,i0))
    if type=='rp':
        f.etat_actuel=i0
        _,module,phase=odeint45_fft(f,yf,np.linspace(ts,ts+T,M),*args,
                                    M=M,T=T,h0=h0)

    vect_freq=np.where(M//2==0,np.linspace(0.,(M/2-1)/(M*h0),M//2),
                          np.linspace(0.,(M-1)/(2*M*h0),M//2))
    if f.freq_constraints!={}:
        for i in f.freq_constraints.keys():
            expression,_=f.freq_constraints[i]
            freq_cstr[i]=expression(module,phase,f.names,vect_freq,1/T)

    if f.constraints!={}:
        for i in f.constraints.keys():
            if isinstance(f.constraints[i][1],tuple):
                _,(_,_,fin,_,_,_)=f.constraints[i]
            else:
                (_,_,fin,_,_,_)=f.constraints[i]
            cstr[i]=fin(ts,cstr[i],T)

    return (ts,yf,cstr,freq_cstr)


@_odeint45_extract_fft.defjvp
def _odeint45_fft_jvp(f,h0,tol,M, primals, tangents):
    y0,T, *args = primals
    delta_y0,dT, *delta_args = tangents
    nargs = len(args)

    def f_aug(y0,delta_y0, t, *args_and_delta_args):
        args,delta_args =args_and_delta_args[:nargs],args_and_delta_args[nargs:]
        primal_dot, tangent_dot = jvp(f.derivative, (y0, t, *args), (delta_y0,
                                                            0., *delta_args))
        return tangent_dot

    yf,cstr,freq_cstr,ts,dts,yf_dot,cstr_dot,freq_delta_cstr=\
        odeint45_extract_fft_etendu(f,f_aug,nargs,h0,tol,M,y0,delta_y0,T,dT,
                                    *args,*delta_args)
    return (ts,yf,cstr,freq_cstr),(dts,yf_dot,cstr_dot,freq_delta_cstr)


def odeint45_extract_fft_etendu(f,f_aug,nargs,h0,tol,M,y0,delta_y0,T,dT,*args):
    args_red = args[:nargs]
    type,cond_stop=f.stop

    def cond_fn(state):
        y_prev2,_,_,y_prev,delta_y_prev, t_prev, h,cstr,_,_ = state
        return (h > 0) & cond_stop(t_prev,t_prev+h,cstr)

    def body_fn(state):
        _,_,_,y_prev,delta_y_prev, t_prev, h,cstr,delta_cstr,i = state

        y,t_now,hopt,inew=next_step_simulation(y_prev,t_prev,i,h,f,tol,h0,
                                                   T,*args_red)

        delta_y=rk_step_der(y_prev,t_prev,delta_y_prev,h,f_aug,*args)

        if f.constraints!={}:
            for i in f.constraints.keys():
                if isinstance(f.constraints[i][1], tuple):
                    test_exp,(_,expression,_,_,der_expression,_)=f.constraints[i]
                else:
                    (_,expression,_,_,der_expression,_)=f.constraints[i]
                    test_exp = lambda t: True
                cstr[i] = np.where(test_exp(t_now),expression(t_prev, y_prev,
                            t_now,y, cstr[i],h,T,f.names),cstr[i])
                delta_cstr[i]= np.where(test_exp(t_now),der_expression(t_prev,
                    y_prev,delta_y_prev, t_now, y,delta_y,cstr[i],delta_cstr[i],
                    h,T,f.names),delta_cstr[i])

        return y_prev,delta_y_prev,t_prev,y, delta_y,t_now, hopt,cstr,\
               delta_cstr,inew

    cstr=dict(zip(list(f.constraints.keys()),[0.]*len(f.constraints)))#INITIALISATION
    delta_cstr=dict(zip(list(f.constraints.keys()),[0.]*len(f.constraints)))
    freq_cstr=dict(zip(list(f.freq_constraints.keys()),
                       [0.]*len(f.freq_constraints)))
    freq_delta_cstr=dict(zip(list(f.freq_constraints.keys()),
                             [0.]*len(f.freq_constraints)))
    if f.constraints!={}:
        for i in f.constraints.keys():
            if isinstance(f.constraints[i][1], tuple):
                test_exp,(init,_,_,dinit,_,_) = f.constraints[i]
            else:
                (init,_,_,dinit,_,_) = f.constraints[i]
                test_exp = lambda t: True
            cstr[i] = np.where(test_exp(0.),init(y0,0.,h0,f.names),cstr[i])
            delta_cstr[i]=np.where(test_exp(0.),dinit(y0,delta_y0,0.,h0,f.names),
                                     delta_cstr[i])

    for element in f.__dict__.keys(): # pour eviter erreurs de code
        if isinstance(f.__dict__[element],interpreters.ad.JVPTracer):
            f.__dict__[element]=f.__dict__[element].primal
    if hasattr(f,'etat_actuel'):
        i0=f.etat_actuel
    else:
        i0=0
    yfm1,_,_,yf,delta_yf,ts,h,cstr,delta_cstr,ifinal=while_loop(cond_fn,
        body_fn,(y0,delta_y0,0.,y0,delta_y0,0.,h0,cstr,delta_cstr,i0))
    if type=='rp':
        f.etat_actuel=i0
        _,module,phase,_,dmodule,dphase=odeint45_fft_etendu(f,f_aug,nargs,h0,
                     tol,M,yf,delta_yf,np.linspace(ts,ts+T,M),T,*args)

    vect_freq=np.where(M//2==0,np.linspace(0.,(M/2-1)/(M*h0),M//2),
                          np.linspace(0.,(M-1)/(2*M*h0),M//2))
    if f.freq_constraints!={}:
        for i in f.freq_constraints.keys():
            _,der_expression=f.freq_constraints[i]
            freq_cstr[i],freq_delta_cstr[i]=der_expression(module,phase,dmodule,
                                            dphase,f.names,vect_freq,1//T)

    if f.constraints!={}:
        for i in f.constraints.keys():
            if isinstance(f.constraints[i][1],tuple):
                _,(_,_,fin,_,_,der_fin)=f.constraints[i]
            else:
                (_,_,fin,_,_,der_fin)=f.constraints[i]
            cstr[i]=fin(ts,cstr[i],T)
            delta_cstr[i]=der_fin(ts,cstr[i],T,delta_cstr[i],dT,yf,f.names)

    if type=='rp': # partial derivatives of ts
        f.etat_actuel=ifinal
        ind_rp=f.names.index(f.last_var_bf_rp)
        yseuil=f.derivative(yf,ts,*args_red)[ind_rp]
        dts=-(1/yseuil)*delta_yf[ind_rp]
    else:
        dts=0.
    return yf,cstr,freq_cstr,ts,dts,delta_yf,delta_cstr,freq_delta_cstr


################################################################################

def Max_module_freq(ind):
    def expression(module,phase,names,vect_freq,f):
        indf=np.argmin(np.abs(vect_freq-f))
        res=module[names.index(ind),indf]
        return res
    def der_expression(module,phase,dmodule,dphase,names,vect_freq,f):
        indf=np.argmin(np.abs(vect_freq-f))
        res,dres=module[names.index(ind),indf],dmodule[names.index(ind),indf]
        return res,dres
    return expression,der_expression

def Module_Harmoniques(ind,number):
    def expression(module,phase,names,vect_freq,f):
        res=np.zeros(number)
        for j in range(len(res)):
            indf=np.argmin(np.abs(vect_freq-(j+2)*f))
            res=res.at[j].set(module[names.index(ind),indf])
        return res
    def der_expression(module,phase,dmodule,dphase,names,vect_freq,f):
        res = np.zeros(number)
        dres=np.zeros(number)
        for j in range(len(res)):
            indf=np.argmin(np.abs(vect_freq-(j+2)*f))
            res=res.at[j].set(module[names.index(ind),indf])
            dres=dres.at[j].set(dmodule[names.index(ind),indf])
        return res,dres
    return expression,der_expression
