#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import re
from parser.xunit import throw_if_some_failed, parse_last_modified, parse_junit_test_results, open_file


def rubocop_validate_files(files):
    filtered = []
    for file in files:
        if str(file).endswith("csv"):
            filtered.append(file)
    throw_if_some_failed(files, filtered)


def rubocop_iterate_test_cases(file):
    """
    Iterate all test cases found in `file`.
    :param file:
    :return: a list/iterator of tuples (test case node, test hierarchy path)
    """
    with open_file(file) as data_file:
        content = data_file.readlines()
        for line in content:
            match_obj = re.match( r'^(FC[0-9]+): (.*): ([^:]+):([0-9]+)$', line)
            yield (line, (match_obj.group(1), match_obj.group(3), match_obj.group(4)))


def rubocop_duration(splitResult):
    return 0


def rubocop_result(scenario):
    match_obj = re.match( r'^(FC[0-9]+): (.*): ([^:]+):([0-9]+)$', scenario)
    if match_obj.group(1):
        return "FAILED"
    else:
        return "OTHER"
    return "PASSED"

def rubocop_failure_reason(scenario):
    match_obj = re.match( r'^(FC[0-9]+): (.*): ([^:]+):([0-9]+)$', scenario)
    error_message = "%s - %s" % (match_obj.group(1), match_obj.group(2))
    unicode_error_message = unicode(error_message, "utf-8")
    return unicode_error_message.encode("ascii", "xmlcharrefreplace")

def rubocop_custom_properties(scenario, file):
    match_obj = re.match( r'^(FC[0-9]+): (.*): ([^:]+):([0-9]+)$', scenario)
    return {
        "code": match_obj.group(1),
        "description": match_obj.group(2),
        "file": match_obj.group(3),
        "line": match_obj.group(4)
    }


def rubocop_last_modified(file):
    return file.lastModified()


rubocop_validate_files(files)

last_modified = parse_last_modified(files, extract_last_modified=rubocop_last_modified)

print 'LAST MOD', last_modified, test_run_historian.isKnownKey(str(last_modified))
if not test_run_historian.isKnownKey(str(last_modified)):
    events = parse_junit_test_results(files, last_modified,
                                      iterate_test_cases=rubocop_iterate_test_cases,
                                      extract_duration=rubocop_duration,
                                      extract_result=rubocop_result,
                                      extract_failure_reason=rubocop_failure_reason,
                                      extract_custom_properties=rubocop_custom_properties)
    print 'built run with events', events
else:
    events = []

# Result holder should contain a list of test runs. A test run is a list of events

result_holder.result = [events] if events else []
