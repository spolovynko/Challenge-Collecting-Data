import re
def table_reader(string, ls, url, data):
        if url.findAll("th",text=re.compile(string)):
            for table in url.findAll("th",text=re.compile(string)):
                    return data[ls].append(table.find_next("td").next_element.strip())
        else:
            return data[ls].append(None)