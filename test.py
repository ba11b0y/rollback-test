import rollbar

rollbar.init('7fc34f84b7694c0ab3dd87fe3a56e9dd')

try:
    b = a + 1
except:
    rollbar.report_exc_info()
