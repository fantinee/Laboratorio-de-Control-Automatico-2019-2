% Repetir una PRBS 20 veces
prbs_N = (2^12)-1;
u = idinput(prbs_N, 'prbs', [0 1], [-1 1])';
u_20 = repmat(u, 1, 20)';

% Simular Planta con entrada u_20
Kp = 0.3;
Ts = 0.005;           
tfinal = (prbs_N*Ts)*20;
t = (0:Ts:tfinal-Ts)';
npts = length(t);
u_in = [t u_20];
[t_out, x, y] = sim('StablePlant', tfinal, [], u_in);

y_detrend = detrend(y);


% Ploteo
figure
grid on
plot(t_out, y_detrend)
title('Respuesta a u1')
xlabel('t')
ylabel('Magnitud')




