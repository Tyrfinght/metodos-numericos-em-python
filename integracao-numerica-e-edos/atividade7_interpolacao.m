x1 = 0:0.1:1;
x2 = 1:0.1:2;

d1 = @(x) -2 + (x - x); 
d2 = @(x) 6*x - 8;

plot(x1, d1(x1), '.b;p1''(x);', x2, d2(x2), '.g;p2''(x);', 'markersize', 12);
ylim([-4 4]);
xlabel('x');
ylabel('s''(x)');
title('Derivada de s(x)');
legend('location', 'northwest');
grid on;