import re
def table_reader(string, ls, url, dicti):
        if url.findAll("th",text=re.compile(string)):
            for table in url.findAll("th",text=re.compile(string)):
                    return dicti[ls].append(table.find_next("td").next_element.strip())
        else:
            return dicti[ls].append(None)