function [corr] = cyclic_autocorrelation(vector)
    corr = zeros(1, length(vector));
    vector_2 = vector;
    for k=1:length(vector)
        corr(k) = vector * (vector_2)';
        vector_2 = [vector_2(end), vector_2(1:end-1)];
    end
end

