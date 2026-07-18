#!/usr/bin/env python3
"""Merge staged agent rows into coding-sheet.csv with DOI dedup, then print matrices.
Usage: put new rows (no header) in staging.csv, then run: python3 merge.py
"""
import csv, sys, os
from collections import defaultdict

HEADER=["id","authors","year","journal","doi","ajg_rank","found_via","theory_code","theory_secondary","context_locus","context_role_structure","context_geography","context_sample","focal_construct","problem_code","problem_secondary","key_finding","mechanism","design","data_source","analysis","outcome_valence","screening_decision","memo"]

def load(path):
    if not os.path.exists(path): return []
    return list(csv.reader(open(path)))

def main():
    existing=list(csv.DictReader(open('coding-sheet.csv')))
    seen_doi={r['doi'] for r in existing if r['doi']}
    seen_key={(r['authors'].lower().strip(),r['year']) for r in existing if r['authors']}

    staged=load('staging.csv')
    added=[]; dropped_dup=0; dropped_bad=0
    with open('coding-sheet.csv','a',newline='') as f:
        w=csv.writer(f)
        for row in staged:
            if not row or row[0].strip() in ('','id','NONE'):
                dropped_bad+=1; continue
            if len(row)<len(HEADER):
                row=row+['']*(len(HEADER)-len(row))
            elif len(row)>len(HEADER):
                row=row[:len(HEADER)]
            doi=row[4].strip()
            key=(row[1].lower().strip(),row[2].strip())
            if doi and doi in seen_doi: dropped_dup+=1; continue
            if not doi and key in seen_key: dropped_dup+=1; continue
            w.writerow(row); added.append(row)
            if doi: seen_doi.add(doi)
            seen_key.add(key)
    print(f"added={len(added)} dup_skipped={dropped_dup} blank_skipped={dropped_bad}")
    matrices()

def matrices():
    rows=list(csv.DictReader(open('coding-sheet.csv')))
    sample=[r for r in rows if r['screening_decision'] in ('A','B') and r['problem_code'] not in ('','review')]
    print(f"\n=== in-sample coded: {len(sample)} ===")
    loci=['independent','academic','corporate','family','platform','social','multiple','other']
    probs=['ACTION','HIERARCHY','PROTOTYPE','VALUES','AUDIENCE','PERSISTENCE','OTHER']
    M=defaultdict(lambda:defaultdict(int))
    for r in sample: M[r['context_locus']][r['problem_code']]+=1
    print("\nRQ1 Problem x Locus")
    print("problem".ljust(12)+"".join(l[:6].rjust(7) for l in loci))
    for p in probs:
        print(p.ljust(12)+"".join(str(M[l][p]).rjust(7) for l in loci))
    print("\nDominant problem per locus:")
    for l in loci:
        d=M[l];
        if sum(d.values())==0: continue
        top=max(d.items(),key=lambda x:x[1])
        share=top[1]/sum(d.values())
        print(f"  {l:12} n={sum(d.values()):3}  dominant={top[0]}({top[1]}, {share:.0%})  {dict(d)}")
    # theory
    th=['SIT','RIT','NARR','POSS','IDWORK','IMPR','CONFLICT','FIT','OTHER']
    T=defaultdict(lambda:defaultdict(int))
    for r in sample:
        for t in (r['theory_code'],r['theory_secondary']):
            if t in th: T[r['context_locus']][t]+=1
    print("\nRQ2 Theory x Locus (incl. secondary)")
    print("theory".ljust(10)+"".join(l[:6].rjust(7) for l in loci))
    for t in th:
        print(t.ljust(10)+"".join(str(T[l][t]).rjust(7) for l in loci))
    # role structure
    rs=defaultdict(int)
    for r in sample: rs[r['context_role_structure']]+=1
    print("\nRole structure:",dict(rs))

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='matrices': matrices()
    else: main()
