% =========================================================================
% AJUSTE DE CURVAS: MÉTODO DOS MÍNIMOS QUADRADOS (OCTAVE)
% Modelo Exponencial - Consumo de Energia Elétrica
% =========================================================================


x = [1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12];
y = [140; 220; 150; 170; 190; 180; 170; 160; 180; 200; 170; 199];

phie1 = @(x) exp(-x);
phie2 = @(x) ones(length(x), 1);
phie3 = @(x) exp(x);

Pe = [phie1(x) phie2(x) phie3(x)];

% Ae * ce = be => (Pe' * Pe) * ce = Pe' * y
Ae = Pe' * Pe;
be = Pe' * y;
ce = Ae \ be;

phie_fit = @(xx) ce(1)*phie1(xx) + ce(2)*phie2(xx) + ce(3)*phie3(xx);

norma_exponencial = norm(phie_fit(x) - y)^2;
fprintf('Residuo Quadratico (Modelo Exponencial): %.1f\n', norma_exponencial);

xx = linspace(0, 12, 60)';
plot(x, y, 'x', xx, phie_fit(xx), 'm');
title('Ajuste Exponencial - Consumo de Energia');
xlabel('Mês');
ylabel('Consumo (KWh)');
legend('Dados Reais', 'Ajuste Exponencial');