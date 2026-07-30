N = 10000;
valor_exato_teorico = single((pi^2) / 8); % Convergência da série infinita

fprintf('Valor teórico exato da série: %.10f\n\n', valor_exato_teorico);

% 1. ALGORITMO DE SOMA CRESCENTE
soma_crescente = single(0.0);

for k = 1:N
    termo = single(1.0 / (2*k - 1)^2);
    soma_crescente = soma_crescente + termo;
end

erro_crescente = abs(valor_exato_teorico - soma_crescente);
fprintf('--- ALGORITMO 1: SOMA CRESCENTE ---\n');
fprintf('Resultado Obtido: %.10f\n', soma_crescente);
fprintf('Erro Absoluto:    %.4e\n\n', erro_crescente);


% 2. ALGORITMO DE SOMA DECRESCENTE
soma_decrescente = single(0.0);

for k = N:-1:1
    termo = single(1.0 / (2*k - 1)^2);
    soma_decrescente = soma_decrescente + termo;
end

erro_decrescente = abs(valor_exato_teorico - soma_decrescente);
fprintf('--- ALGORITMO 2: SOMA DECRESCENTE ---\n');
fprintf('Resultado Obtido: %.10f\n', soma_decrescente);
fprintf('Erro Absoluto:    %.4e\n\n', erro_decrescente);


% 3. ANÁLISE COMPARATIVA
disp('--- ANÁLISE ---');
if erro_decrescente < erro_crescente
    disp('A soma decrescente minimizou a perda de dígitos significativos,');
    disp('pois somou valores de grandezas parecidas antes de adicioná-los');
    disp('aos termos de maior peso.');
end