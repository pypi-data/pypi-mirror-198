import numpy as np
from noloadj.ODE.ode45 import *

def odeint45_fft(f,y0,t,*args,M,T=0.,h0=1e-5,tol=1.48e-8):
    return _odeint45_fft(f,h0,tol,M,y0,t,T,*args)


@partial(custom_jvp,nondiff_argnums=(0,1,2,3))
def _odeint45_fft(f,h0,tol,M,y0,t,T,*args):

    def scan_fun(state,t):

        def cond_fn(state):
            _,_,y_prev,t_prev,h,_=state
            return (t_prev<t) & (h>0)

        def body_fn(state):
            _,_,y_prev,t_prev,h,i=state

            y,t_now,hopt,inew=next_step_simulation(y_prev,t_prev,i,h,f,tol,h0,
                                                   T,*args)

            return y_prev,t_prev,y,t_now,hopt,inew

        y_prev, t_prev, y_now, t_now, h, i = while_loop(cond_fn, body_fn, state)
        # interpolation lineaire
        y = ((y_prev-y_now) * t + t_prev *y_now-t_now *y_prev)/(t_prev-t_now)
        return (y_prev, t_prev, y, t, h, i), y

    if hasattr(f,'etat_actuel'):
        i0=f.etat_actuel
    else:
        i0=0
    _,ys=scan(scan_fun,(y0,t[0],y0,t[0],h0,i0),t[1:])
    ys=np.transpose(np.concatenate((y0[None], ys)))
    yfft=np.fft.fft(ys,M)/M # fft avec normalisation
    module,phase=np.abs(yfft)*2,np.angle(yfft) # amplitude et phase de la fft
    return ys,module[:,0:M//2],phase[:,0:M//2] # on retire les frequences negatives


@_odeint45_fft.defjvp
def _odeint45_fft_jvp(f,h0,tol,M, primals, tangents):
    y0, t,T, *args = primals
    delta_y0, _,_, *delta_args = tangents
    nargs = len(args)

    def f_aug(y0,delta_y0, t, *args_and_delta_args):
        args,delta_args=args_and_delta_args[:nargs], args_and_delta_args[nargs:]
        primal_dot, tangent_dot = jvp(f.derivative, (y0, t, *args), (delta_y0,
                                                    0., *delta_args))
        return tangent_dot

    ys,module,phase,ys_dot,dmodule,dphase = odeint45_fft_etendu(f,f_aug,nargs,
                    h0,tol,M, y0,delta_y0,t,T, *args, *delta_args)
    return (ys,module,phase),(ys_dot,dmodule,dphase)


def odeint45_fft_etendu(f,f_aug,nargs,h0,tol,M,y0,delta_y0,t,T,*args):
    args_red = args[:nargs]

    def scan_fun(state, t):

        def cond_fn(state):
            _,_,_,y_prev,delta_y_prev, t_prev, h,_ = state
            return (t_prev < t) & (h > 0)

        def body_fn(state):
            _,_,_,y_prev,delta_y_prev, t_prev, h,i = state

            y,t_now,hopt,inew=next_step_simulation(y_prev,t_prev,i,h,f,tol,h0,
                                                   T,*args_red)

            delta_y=rk_step_der(y_prev,t_prev,delta_y_prev,h,f_aug,*args)

            return y_prev,delta_y_prev,t_prev,y,delta_y,t_now,hopt,inew

        y_prev, delta_y_prev, t_prev, y_now, delta_y_now, t_now, h, i = \
            while_loop(cond_fn, body_fn, state)
        # interpolation lineaire
        y = ((y_prev-y_now)*t +t_prev * y_now - t_now * y_prev)/(t_prev-t_now)
        delta_y = ((delta_y_prev - delta_y_now) * t +t_prev*delta_y_now-t_now *
                   delta_y_prev) / (t_prev - t_now)
        return (y_prev, delta_y_prev, t_prev, y, delta_y, t, h, i), (y, delta_y)

    for element in f.__dict__.keys(): # pour eviter erreurs de code
        if isinstance(f.__dict__[element],interpreters.ad.JVPTracer):
            f.__dict__[element]=f.__dict__[element].primal
    if hasattr(f,'etat_actuel'):
        i0=f.etat_actuel
    else:
        i0=0
    _, (ys,delta_ys)=scan(scan_fun,(y0,delta_y0,t[0],y0,delta_y0,t[0],h0,i0),
                          t[1:])
    ys=np.transpose(np.concatenate((y0[None], ys)))
    delta_ys=np.transpose(np.concatenate((delta_y0[None], delta_ys)))
    yfft = np.fft.fft(ys, M) / M  # fft avec normalisation
    dyfft=np.fft.fft(delta_ys,M)/M
    module,phase=np.abs(yfft)*2,np.angle(yfft)  # amplitude et phase de la fft
    dmodule,dphase=np.abs(dyfft)*2,np.angle(yfft)
    return ys,module[:,0:M//2],phase[:,0:M//2],delta_ys,dmodule[:,0:M//2],\
           dphase[:,0:M//2]


