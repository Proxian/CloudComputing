#number5code

np = 1e3; nd = 2;
hp = gcp('nocreate');
if isempty(hp), hp = parpool(8); end
A = randn(np, nd); B = randn(np, nd);
dA = distributed(A); dB = distributed(B);
tic;
c = sqrt(sum((A-B).^2,2));
d = gather(c);
t = toc;
display(t);
