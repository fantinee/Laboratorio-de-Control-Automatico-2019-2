function [vector] = vector_averager(matrix)
    matrix_size = size(matrix);
    vector = matrix * ones(matrix_size(2), 1) / matrix_size(2);
end

