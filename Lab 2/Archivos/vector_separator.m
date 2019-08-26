function [matrix] = vector_separator(vector, divisions)
    matrix = zeros(length(vector)/divisions, divisions);
    minivector_size = length(vector) / divisions;
    for k=1:divisions
        matrix(:,k) = vector(1, (k-1) * minivector_size + 1: k * minivector_size);
    end
end

