class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False
        return True
    

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team
    

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def test(self, player):
        return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        if not self._matcher.test(player):
            return True
        return False


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False
    
class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matchers = And(matcher)

    def build(self):
        return self._matchers
    
    def plays_in(self, team):
        return QueryBuilder(And(self._matchers, PlaysIn(team)))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._matchers, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._matchers, HasFewerThan(value, attr)))

    def one_of(self, *querys):
        return QueryBuilder(Or(*querys))
