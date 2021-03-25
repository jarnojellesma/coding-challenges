=begin
You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

Credits: Daily Coding Problem.
=end

def count_coins_helper(matrix, visited, curr_row, curr_col)
    visited << matrix[curr_row][curr_col]
    right_coins = -1
    down_coins = -1

    if curr_col + 1 < matrix[curr_row].length()
        right_coins = count_coins_helper(matrix, visited.dup, curr_row, curr_col + 1)
    end

    if curr_row + 1 < matrix.length()
        down_coins = count_coins_helper(matrix, visited.dup, curr_row + 1, curr_col)
    end
    
    right_down_max = [right_coins, down_coins].max

    return right_down_max unless right_down_max < 0

    return visited.reduce(0, :+)
end

def count_coins(matrix)
   return count_coins_helper(matrix, [], 0, 0)
end

RSpec.describe do
    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1]
    ]

    it "returns the maximum amount of coins" do
        coins = count_coins(matrix)
        expect(coins).to eq(12)
    end
end
    
