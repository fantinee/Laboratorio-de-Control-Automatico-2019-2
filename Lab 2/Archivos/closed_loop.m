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

% Filtrar el drift
y_detrend = detrend(y);
% Cortar vector y transponer
y_detrend = y_detrend(length(y_detrend)-length(t)+1:length(y_detrend))';

% Ploteo salida planta
figure
grid on
plot(t, y_detrend)
title('Salida y')
xlabel('t')
ylabel('Magnitud')

% Filtro ruido blanco
y_sep = vector_separator(y_detrend, 20);
y_filtered = vector_averager(y_sep(:,2:end));
t_filtered = (0:Ts:(length(y_filtered)*Ts-Ts))';

% Ploteo PRBS filtrada
figure
grid on
plot(t_filtered, y_filtered)
title('PRBS filtrada')
xlabel('t')
ylabel('Magnitud')
