separators = [',', ';', ':']
terminals = ['.', '?', '!']
space = ' '


def validate_sentence(sentence)
    
    sentence.split('').each { |char|
        puts char    
    }
    
    return false
end

RSpec.describe do
    it "returns true if the sentence is valid" do
        is_valid = validate_sentence("Hello world!")
        expect(is_valid).to eq(true)
    end
end
    
