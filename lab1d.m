#number4code

np = 1e3; nd = 2;
spmd
    tic;
    A = randn(np/8, nd); B = randn(np/8, nd);
    d = zeros(np/8, 1);
    
    for i = 1:np/8
        for j = 1:nd
            d(i) = (B(i, 1) -A(i,1)).^2 + (B(i, 2) -A(i,2)).^2;
        end
        d(i) = sqrt(d(i));
    end
t = toc;
display(t);
end 
da = gcat(d,1,1);
