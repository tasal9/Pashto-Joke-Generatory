import sys
import os

HERE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, HERE)

from generator import get_random_joke


def test_returns_dict():
    j = get_random_joke('jokes.json')
    assert isinstance(j, dict), 'Expected dict'


def test_has_keys():
    j = get_random_joke('jokes.json')
    assert 'type' in j, 'Missing type key'
    if j['type'] == 'single':
        assert 'joke' in j, 'single joke missing text'
    elif j['type'] == 'twopart':
        assert 'setup' in j and 'delivery' in j, 'twopart missing parts'


def test_randomness():
    seen = set()
    for _ in range(10):
        j = get_random_joke('jokes.json')
        seen.add(j.get('joke') or (j.get('setup') + '|' + j.get('delivery')))
    assert len(seen) >= 2, 'Randomness: expected at least 2 different jokes in 10 picks'


def run_all():
    tests = [test_returns_dict, test_has_keys, test_randomness]
    passed = 0
    failed = []
    for t in tests:
        try:
            t()
            print(f'PASS: {t.__name__}')
            passed += 1
        except AssertionError as e:
            print(f'FAIL: {t.__name__} - {e}')
            failed.append((t.__name__, str(e)))
    print('\nSummary:')
    print(f'  Passed: {passed}/{len(tests)}')
    if failed:
        print('  Failures:')
        for name, msg in failed:
            print(f'   - {name}: {msg}')
        sys.exit(1)


if __name__ == '__main__':
    run_all()
