#!/usr/bin/python
import sys
import numpy as np
import collections
import csv
from itertools import islice

def argv_provided():
    return len(sys.argv) > 1

log_file_path = 'log.txt'

title_list = []
content_list = []
if argv_provided():
    in_file_path = ' '.join(sys.argv[1:])
    with open(in_file_path) as in_file:
        for line in in_file.readlines():
            if '>' in line:
                title_list.append(line)
            else:
                content_list.append(line)

    sequence_size = len(content_list[0])-1
    num_of_sequences = len(content_list)

    sequences_matrix = np.array([[content_list[row][col] for col in range(sequence_size)] for row in range(num_of_sequences)])
    # 1 residue per line
    residues_matrix = np.transpose(sequences_matrix)
    residues_report = []
    with open(log_file_path, 'w') as log_file:
        for res_index, residue in enumerate(residues_matrix):
            A, T, C, G, O = 0, 0, 0, 0, 0
            for base_index, base in enumerate(residue):
                if base == 'A': A += 1
                elif base == 'T': T += 1
                elif base == 'C':  C += 1
                elif base == 'G': G += 1
                else:
                    O += 1
                    log_file.write('Found residue {} in (sequence, index) : ({}, {})\n'.format(base, base_index, res_index))

            residues_report.append([A, T, C, G, O])

    with open('residue_report.csv', 'w', newline='') as csv_output:
        csv_writer = csv.writer(csv_output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['ID', 'A', 'A%', 'T', 'T%', 'C', 'C%', 'G', 'G%', 'O', 'O%'])
        print('Residue #: A, A%, T, T%, C, C%, G, G%, O, O%')
        for index, residue in enumerate(residues_report):
            A_absolute = residue[0]
            T_absolute = residue[1]
            C_absolute = residue[2]
            G_absolute = residue[3]
            O_absolute = residue[4]
            A_percentage = A_absolute / num_of_sequences
            T_percentage = T_absolute / num_of_sequences
            C_percentage = C_absolute / num_of_sequences
            G_percentage = G_absolute / num_of_sequences
            O_percentage = O_absolute / num_of_sequences
            formatted_output_line = '{i:5d} : {aabs:5d}, {aper:6.2%}, {tabs:5d}, {tper:6.2%}, {cabs:5d}, {cper:6.2%}, {gabs:5d}, {gper:6.2%}, {oabs:5d}, {oper:6.2%}'.format(
                i=index,
                aabs=A_absolute, aper=A_percentage,
                tabs=T_absolute, tper=T_percentage,
                cabs=C_absolute, cper=C_percentage,
                gabs=G_absolute, gper=G_percentage,
                oabs=O_absolute, oper=O_percentage
            )
            csv_output_line = [index+1, A_absolute, A_percentage, T_absolute, T_percentage, C_absolute, C_percentage, G_absolute, G_percentage, O_absolute, O_percentage]
            #csv_writer.writerow(formatted_output_line.replace(' ', '').replace(':', ',').replace('%', ''))
            csv_writer.writerow(csv_output_line)
            print(formatted_output_line)

        print('Sequences size: {}'.format(sequence_size))
        print('Number of sequences: {}'.format(num_of_sequences))
        print('Residues count: {}'.format(len(residues_report)))
else:
    print('File\'s  path has not been provided.')
