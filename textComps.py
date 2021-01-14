stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
punct_list = [",",".","!","?"]

def clean_samples(sample):
    sample_clean = " "+sample.lower()+" "
    for i in stop_words:
        sample_clean = sample_clean.replace(" "+i+" "," ")
    for i in punct_list:
        sample_clean = sample_clean.replace(i,"")
    sample_clean = sample_clean.strip()
    sample_clean = sample_clean.split(" ")
    return sample_clean


def comp_samples(sample1,sample2,default_values=True):
    sample1 = clean_samples(sample1)
    sample2 = clean_samples(sample2)
    
    s1_diff_s2 = len(set(sample1)-set(sample2))
    s2_diff_s1 = len(set(sample2)-set(sample1))
    total_words = len(sample1)+len(sample2)
    similar_pct = (total_words-s1_diff_s2-s2_diff_s1)/total_words
    
    return "Similarity between two provided samples is: " + str(similar_pct)