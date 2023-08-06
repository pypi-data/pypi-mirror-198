import pysam
import pysamstats
from collections import Counter

bam = "/omics/odcf/project/hipo/hipo_021/sequencing/whole_genome_sequencing/view-by-pid/H021-3UN257/tumor02/paired/merged-alignment/.merging_0/tumor02_H021-3UN257_merged.mdup.bam"
infile = pysam.AlignmentFile(bam, "rb")
#outfile = pysam.AlignmentFile("tmp_file.sam", "w")

position = 13273
count = Counter()

for pileupcolumn in infile.pileup("1", position - 1, position, stepper = 'samtools'):
  for read in pileupcolumn.pileups:
    if not read.is_del and not read.is_refskip:
      #print(read.alignment.query_sequence
      #print(read.alignment.query_sequence[read.query_position])
      #print(read.alignment.query_position)
      #print(read.alignment.query_name, read.alignment.query_sequence[read.query_position], read.query_position)

      count[read.alignment.query_sequence[read.query_position]] += 1

print(count)
  
print(dir(pysamstats))
# iterate over statistics, one record at a time
for rec in pysamstats.stat_variation(bam, 
                                      chrom='1', 
                                      start=position-1, 
                                      end=position,
                                      min_baseq = 13,
                                      min_mapq = 30,
                                      fafile='/omics/odcf/reference_data/legacy/ngs_share/assemblies/hg19_GRCh37_1000genomes/sequence/1KGRef_Phix/hs37d5_PhiX.fa'):
  print(rec)
    #print(rec['chrom'], rec['pos'], rec['reads_all'], rec['reads_pp'], rec['matches'], rec['mismatches'], rec['deletions'], rec['insertions'], rec['coverage'])