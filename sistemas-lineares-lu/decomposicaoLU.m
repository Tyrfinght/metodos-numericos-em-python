A = rand(n);
H = hilb(n);

e_vec = ones(n, 1);
b = A * e_vec;
c = H * e_vec;

[L_A, U_A, P_A] = lu(A);
[L_H, U_H, P_H] = lu(H);

y_A = L_A \ (P_A * b);
x_A = U_A \ y_A;

y_H = L_H \ (P_H * c);
x_H = U_H \ y_H;

erro_relativo_A = norm(A * x_A - b) / norm(x_A);
erro_relativo_H = norm(H * x_H - c) / norm(x_H);

fprintf('Erro Relativo na Matriz Aleatória: %e\n', erro_relativo_A);
fprintf('Erro Relativo na Matriz de Hilbert: %e\n', erro_relativo_H);

B = zeros(n);
I = eye(n);
for k = 1:n
    y_inv = L_A \ (P_A * I(:, k));
    B(:, k) = U_A \ y_inv;
end

erro_inversa = norm(B - inv(A)) / norm(B);
identidade_aprox = A * B;
erro_identidade = norm(identidade_aprox - I) / norm(I);

fprintf('Qualidade da Inversa (Norma do Resíduo): %e\n', erro_inversa);
fprintf('Teste A * A^(-1) = I (Erro): %e\n', erro_identidade);