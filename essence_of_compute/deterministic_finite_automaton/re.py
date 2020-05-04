from nfa import NFARulebook, NFADesign, FARule


class Pattern(object):
    precedence = 0

    def bracket(self, outer_precedence):
        if self.precedence < outer_precedence:
            return '({})'.format(self.__str__())
        else:
            return self.__str__()

    def match(self, string):
        return self.to_nfa_design().is_accepting(string)

class Empty(Pattern):
    precedence = 3

    def __str__(self):
        return ''

    def to_nfa_design(self):
        start_state = type('', (), {})() 
        accept_states = [start_state]
        nfa = NFADesign(start_state, accept_states, NFARulebook([]))
        return nfa


class Literal(Pattern):
    precedence = 3

    def __init__(self, character):
        self.character = character

    def __str__(self):
        return '{}'.format(self.character)
    
    def to_nfa_design(self):
        start_state = type('', (), {})()
        accept_states = type('', (), {})()
        rule = FARule(start_state, self.character, accept_states)
        rulebook = NFARulebook([rule])
        nfa = NFADesign(start_state, [accept_states], rulebook)
        return nfa


class Concatenate(Pattern):
    precedence = 1

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "{}".format(''.join([self.first.bracket(self.precedence),
                                    self.second.bracket(self.precedence)]))

    def to_nfa_design(self):
        first_nfa_design = self.first.to_nfa_design()
        second_nfa_design = self.second.to_nfa_design()

        start_state = first_nfa_design.start_state
        accept_states = second_nfa_design.accept_state
        rules = first_nfa_design.rulebook.rules + second_nfa_design.rulebook.rules
        extra_rules =[FARule(state, None, second_nfa_design.start_state) for \
                      state in first_nfa_design.accept_state]
        rulebook = NFARulebook(rules + extra_rules)
        return NFADesign(start_state, accept_states, rulebook)



class Choose(Pattern):
    precedence = 1

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "{}".format('|'.join([self.first.bracket(self.precedence),
                                     self.second.bracket(self.precedence)]))


class Repeat(Pattern):
    precedence = 2

    def __init__(self, pattern):
        self.pattern = pattern

    def __str__(self):
        return self.pattern.bracket(self.precedence) + "*"


if __name__ == "__main__":
    '''
    print("-" * 39)
    pattern = Literal('a')
    print("pattern", pattern)
    print('match', pattern.match('a'))
    print('match', pattern.match(''))
    print("-" * 39)
    pattern = Empty()
    print("match", pattern.match(""))
    print("-" * 39)
    print("match", pattern.match("a"))
    print("-" * 39)
    pattern = Literal('a')
    print("pattern", pattern)
    print('match', pattern.match('a'))
    print("-" * 39)
    pattern = Concatenate(Literal('a'), Literal('b'))
    print("pattern", pattern)
    print("match", pattern.match('a'))
    print("match", pattern.match('ab'))
    print("match", pattern.match('abc'))

    print("-" * 39)
    pattern = Repeat(
        Choose(
            Concatenate(Literal('a'), Literal('b')),
            Literal('a')
        )
    )

    print('pattern', pattern)
    
    nfa_design = Empty().to_nfa_design()
    print(nfa_design.is_accepting(""))
    print(nfa_design.is_accepting("a"))

    nfa_design = Literal('a').to_nfa_design()
    print(nfa_design.is_accepting(""))
    print(nfa_design.is_accepting("a"))
    print(nfa_design.is_accepting("b"))
    '''
    print("-" * 39)
    pattern = Concatenate(Literal('a'), Literal('b'))
    print("pattern", pattern)
   # print("match", pattern.match('a'))
    print("match", pattern.match(''))
    print("match", pattern.match('abc'))
