%  MÉTODO DE NEWTON
f = @(x) [x(1)^2 + x(2)^2 - x(3); 
          (1/4)*x(1)^2 + (1/9)*x(2)^2 + x(3)^2 - 1; 
          x(1) + x(2)];

j = @(x) [2*x(1), 2*x(2), -1; 
          (1/2)*x(1), (2/9)*x(2), 2*x(3); 
          1, 1, 0];

x0 = [6; -6; 6]; % Ponto inicial
k_newton = 0;

while (norm(f(x0), inf) > 1e-14)
    s = j(x0) \ (-f(x0));
    x0 = x0 + s;
    k_newton = k_newton + 1;
end

fprintf('--- METODO DE NEWTON ---\n');
fprintf('Iterações: %d\n', k_newton);
fprintf('Norma do erro: %e\n', norm(f(x0), inf));
disp('Raiz encontrada:');
disp(x0);

% MÉTODO DE GAUSS-SEIDEL ADAPTADO
x0_seidel = [6; -6; 6];
x3 = x0_seidel;
k_seidel = 0;

a = @(x) [x(1)^2 + x(2)^2 - x(3)];
b = @(x) [(1/4)*x(1)^2 + (1/9)*x(2)^2 + x(3)^2 - 1];
c = @(x) [x(1) + x(2)];

while (norm(f(x3), inf) > 1e-14)
    % Usando fsolve do Octave para simular as iterações de Seidel
    x1 = fsolve(a, x0_seidel);
    x2 = fsolve(b, x1);
    x3 = fsolve(c, x2);
    x0_seidel = x3;
    k_seidel = k_seidel + 1;
end

fprintf('\n--- METODO DE GAUSS-SEIDEL ADAPTADO ---\n');
fprintf('Iterações: %d\n', k_seidel);
fprintf('Norma do erro: %e\n', norm(f(x0_seidel), inf));
disp('Raiz encontrada:');
disp(x0_seidel);