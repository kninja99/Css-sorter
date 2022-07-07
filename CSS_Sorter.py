import collections
css_file = open("test.css", 'r')
#content = css_file.read()

lines = css_file.readlines()
# a alphabetical dictonary 
organizer = {}
bracket_counter = 0
# css element split up line byt line 
css_ele = []
for line in lines:
    curr_line = line.replace(' ', '')
    if curr_line != '' and curr_line.split() :
        # adds line to the current element
        css_ele.append(line)
        curr_line = curr_line.replace('\n', '')
        # check to see if its at the end of a element 
        if curr_line[len(curr_line) - 1] == '{':
            bracket_counter += 1
        elif curr_line[0] == '}':
            bracket_counter -= 1
        if curr_line[0] == '}' and bracket_counter <= 0:
            start = css_ele[0]
            # replaceing selectors
            start = start.replace('.', '')
            start = start.replace('#', '')
            # copying the array to it points to a different memory address for all elements
            entry = css_ele.copy()
            # check if the element needs to create a new key
            if start[0] in organizer:
                organizer[start[0]].append(entry)
            else:
                organizer[start[0]] = [entry]
            # clearing current css element for new element
            css_ele.clear()

ordered_organizer = collections.OrderedDict(sorted(organizer.items()))

for key in ordered_organizer:
    print(ordered_organizer[key])
css_file.close()
