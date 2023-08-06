import logging
import sys
import json
from pii_transform.api.e2e import MultiPiiTextProcessor

configfile = sys.argv[1]
infile = sys.argv[2]
outfile = sys.argv[3]

#logging.basicConfig(level="INFO")

proc = MultiPiiTextProcessor(lang=["en", "es"], config=configfile, keep_piic=True)


with open(outfile, "w", encoding="utf-8") as fout:
    with open(infile, encoding="utf-8") as fin:
        for line in fin:
            doc = json.loads(line)
            doc["text"] = proc(doc["text"], lang=doc["lang"])
            json.dump(doc, fout, indent=None, ensure_ascii=False)
            print(file=fout)

stats = proc.stats()
print(stats)

print(list(proc.piic()))
