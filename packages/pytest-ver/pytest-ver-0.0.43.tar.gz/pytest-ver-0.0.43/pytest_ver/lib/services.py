cfg = None

storage = None

proto = None

trace = None

summary = None

logger = None

harness = None

iuv = None


# -------------------
def abort(msg=None):
    # may be called by IUV, by UT, or by normal operation
    if msg is None:
        line = 'abort called'
    else:
        line = f'abort called: {msg}'

    # logger may or may not be defined
    if logger is None:
        print(line)  # pragma: no cover
        # coverage: logger is always defined in IUV
    else:
        logger.err(line)

    import pytest
    if cfg.iuvmode:  # pragma: no cover
        # coverage: iuvmode is only set during IUV and UT runs
        # harness may or may not be defined
        if harness is None:
            # just skip the current testcase
            pytest.skip(line)
        elif harness.iuv is None:
            # UT: skip
            logger.err(f'ut: {msg}')
        else:
            harness.iuv.abort(line)
    else:
        # it's normal operation, end the pytest session
        # coverage: iuvmode is set for IUV and UT runs; never gets here
        pytest.exit(line)  # pragma: no cover
