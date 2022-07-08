import collections
import os
from os.path import exists


def sortCss(css_path):
    css_file = open(css_path, 'r')
    #content = css_file.read()

    lines = css_file.readlines()
    css_file.close()
    # a alphabetical dictonary
    organizer = {}
    bracket_counter = 0
    # css element split up line byt line
    css_ele = []
    for line in lines:
        curr_line = line.replace(' ', '')
        if curr_line != '' and curr_line.split():
            # adds line to the current element
            css_ele.append(line)
            curr_line = curr_line.replace('\n', '')
            # check to see if its at the end of a element
            if curr_line[len(curr_line) - 1] == '{':
                bracket_counter += 1
            elif curr_line[0] == '}':
                bracket_counter -= 1
                css_ele[len(css_ele) - 1] = css_ele[len(css_ele) - 1] + '\n'
            if curr_line[0] == '}' and bracket_counter <= 0:
                # making sure we dont start with a comment line
                for line in css_ele:
                    if line[0] != '/' and line[len(line) -1] != '/':
                        start = line.lower()
                        break
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
    pwd = os.getcwd()
    # removes old sorted css
    if exists(f'{pwd}/sorted.css'):
        os.remove(f'{pwd}/sorted.css')
    css_sorted = open('sorted.css', 'w')
    for key in ordered_organizer:
        # grabs each array of elements that start with this key
        for arr in ordered_organizer[key]:
            # writes each element
            for element in arr:
                css_sorted.write(element)


# for debugging and quick testing
sortCss('test.css')
