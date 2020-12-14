import os
import re
from networkx.algorithms import isomorphism
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic,fast_could_be_isomorphic, could_be_isomorphic, faster_could_be_isomorphic
import numpy as np
import json
import pandas as pd


def graph_data(s1,s2):
    node_pattern="node:\ {.*}"
    edge_pattern="edge:\ {.*}"

    node_sep1=re.findall(node_pattern,s1)
    edge_sep1=re.findall(edge_pattern,s1)
    
    node_sep2=re.findall(node_pattern,s2)
    edge_sep2=re.findall(edge_pattern,s2)

    nodes1=[]
    edges1=[]
    nodes2=[]
    edges2=[]
    for i in node_sep1:
        nodes1.append(re.findall('\".*\"',i.split('label')[0]))

    for i in edge_sep1:
        edges1.append([re.findall('\".*\"',i.split('targetname')[0]),re.findall('\".*\"',str(i.split('targetname')[1]).split('label')[0])])
    
    for i in node_sep2:
        nodes2.append(re.findall('\".*\"',i.split('label')[0]))

    for i in edge_sep2:
        edges2.append([re.findall('\".*\"',i.split('targetname')[0]),re.findall('\".*\"',str(i.split('targetname')[1]).split('label')[0])])

    node_dict={}
    refined_nodes1=[]
    refined_edges1=[]
    refined_nodes2=[]
    refined_edges2=[]

    count=1
    for i in nodes1:
        if i[0] not in node_dict.keys():
            node_dict[i[0]]=count
            count+=1
        refined_nodes1.append(node_dict[i[0]])
    for i in edges1:
        start=i[0][0]
        dest=i[1][0]
        refined_edges1.append([node_dict[start],node_dict[dest]])
    for i in nodes2:
        if i[0] not in node_dict.keys():
            node_dict[i[0]]=count
            count+=1
        refined_nodes2.append(node_dict[i[0]])
    for i in edges2:
        start=i[0][0]
        dest=i[1][0]
        refined_edges2.append([node_dict[start],node_dict[dest]])
    return [refined_nodes1,refined_edges1,refined_nodes2,refined_edges2]

def isomorph(a,b):
    f1=open(a,'r')
    s1=f1.read()
    f2=open(b,'r')
    s2=f2.read()
    output=graph_data(s1,s2)
    refined_nodes1=output[0]
    refined_edges1=output[1]
    refined_nodes2=output[2]
    refined_edges2=output[3]


    G1=nx.DiGraph()
    G2=nx.DiGraph()

    G1.add_nodes_from(refined_nodes1)
    G1.add_edges_from(refined_edges1)
    G2.add_nodes_from(refined_nodes2)
    G2.add_edges_from(refined_edges2)
    return is_isomorphic(G1, G2)

f=open('req_json.json')
f=json.load(f)
prob_id=open('prolemid-submissionid.json')
prob_id=json.load(prob_id)
non_null_prob_id={}
for i in prob_id:
    if i['problem_id']!=None:
        non_null_prob_id[i['id']]=i['problem_id']

count=0
usernames=f.keys()
final_prob_ids={}
flag= True
assigned_ci=0
for i in usernames:
    try:
        req_ids=f[i].keys()
        for j in req_ids:
            flag=True
            ref_ids=f[i][j]
            ref_ids.reverse()
            for k in ref_ids:
                if flag:
                    if isomorph(os.path.join('program_codes',k+'.ci'),os.path.join('program_codes',j+'.ci')):
                        final_prob_ids[j]=non_null_prob_id[k]
                        print(j,' : ',non_null_prob_id[k])
                        assigned_ci+=1
                        print('assigned-ci: ',assigned_ci)
                        flag=False
            print('count: ',count)
            count+=1
    except:
        print('error')

                
f=open('final_prob_id.json','w')
json.dump(final_prob_ids,f)
