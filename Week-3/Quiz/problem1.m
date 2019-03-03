syms x
y1 = normpdf(x, 5, 0.5);
y2 = normpdf(x, 7, 1);
S = solve(2 * y1 == y2, x)
vpa(S)
