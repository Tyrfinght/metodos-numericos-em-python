format long;

f = @(y, t) (4 * t * exp(-t) - 1) * y;
y0 = 2; 

t_21 = linspace(0, 5, 21)';
h_21 = t_21(2) - t_21(1);

y_21 = lsode(f, y0, t_21);

figure;
plot(t_21, y_21, '.-', 'markersize', 12);
title('Trajetória do PVI - EDO');
xlabel('t');
ylabel('y(t)');
grid on;

Qsc_21 = (h_21 / 3) * (y_21(1) + 4 * sum(y_21(2:2:end-1)) + 2 * sum(y_21(3:2:end-2)) + y_21(end));
fprintf('Área sob a curva (21 pontos): %.10f\n\n', Qsc_21);

disp('Calculando erro para alta precisão (6 casas decimais)...');

t_N1 = linspace(0, 5, 10000000)';
h_N1 = t_N1(2) - t_N1(1);
y_N1 = lsode(f, y0, t_N1);
Qsc1 = (h_N1 / 3) * (y_N1(1) + 4 * sum(y_N1(2:2:end-1)) + 2 * sum(y_N1(3:2:end-2)) + y_N1(end));

t_N2 = linspace(0, 5, 9000000)';
h_N2 = t_N2(2) - t_N2(1);
y_N2 = lsode(f, y0, t_N2);
Qsc2 = (h_N2 / 3) * (y_N2(1) + 4 * sum(y_N2(2:2:end-1)) + 2 * sum(y_N2(3:2:end-2)) + y_N2(end));

E = abs(Qsc2 - Qsc1);

fprintf('Qsc1 (Malha Densa 1): %.15f\n', Qsc1);
fprintf('Qsc2 (Malha Densa 2): %.15f\n', Qsc2);
fprintf('Erro E (Diferença):   %.15e\n', E);