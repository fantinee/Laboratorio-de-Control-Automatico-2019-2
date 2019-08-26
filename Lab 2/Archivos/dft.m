function [out] = dft (vector) % periodo unitario
    N = length(vector);
    ExpCoefs = 1:N;
    Kcoefs = 1:N;
    for k = 1:N
        for n = 1: N 
            ExpCoefs(n)=exp(-j*2*pi*((-N/2)+n-1)*((-N/2)+k-1)/N);
        end  
        Kcoefs(k) = sum(vector.*ExpCoefs)/N;
    end
    out = Kcoefs;
end