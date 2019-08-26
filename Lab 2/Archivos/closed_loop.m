% Repetir una PRBS 20 veces
prbs_N = (2^12)-1;
u = idinput(prbs_N, 'prbs', [0 1], [-1 1])';
u_20 = repmat(u, 1, 20)';

% Simular Planta con entrada u_20
Ts = 0.005;           
tfinal = (prbs_N*Ts)*20;
t = (0:Ts:tfinal-Ts)';
npts = length(t);
u_in = [t u_20];
[t_out, x, y] = sim('StablePlant', tfinal, [], u_in);