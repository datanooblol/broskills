from dataclasses import dataclass

@dataclass
class Score:
    precision: float
    recall: float
    fmeasure: float

def exact_match(y_true, y_pred):
    return int((y_true.strip() == y_pred.strip()))

class CustomRouge:
    def rouge1(self, y_true, y_pred):
        ref_count = {}
        for token in y_true:
            ref_count[token] = ref_count.get(token, 0) + 1
        
        overlap = 0
        for token in y_pred:
            if token in ref_count and ref_count[token] > 0:
                overlap += 1
                ref_count[token] -= 1
        
        precision = overlap / len(y_pred) if len(y_pred) > 0 else 0
        recall = overlap / len(y_true) if len(y_true) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        return Score(**{'precision': precision, 'recall': recall, 'fmeasure': f1})
    
    def rouge2(self, y_true, y_pred):
        ref_bigrams = [(y_true[i], y_true[i+1]) for i in range(len(y_true)-1)]
        cand_bigrams = [(y_pred[i], y_pred[i+1]) for i in range(len(y_pred)-1)]
        
        ref_count = {}
        for bigram in ref_bigrams:
            ref_count[bigram] = ref_count.get(bigram, 0) + 1
        
        overlap = 0
        for bigram in cand_bigrams:
            if bigram in ref_count and ref_count[bigram] > 0:
                overlap += 1
                ref_count[bigram] -= 1
        
        precision = overlap / len(cand_bigrams) if len(cand_bigrams) > 0 else 0
        recall = overlap / len(ref_bigrams) if len(ref_bigrams) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        return Score(**{'precision': precision, 'recall': recall, 'fmeasure': f1})
    
    def rougeL(self, y_true, y_pred):
        m, n = len(y_true), len(y_pred)
        lcs = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if y_true[i-1] == y_pred[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        
        lcs_length = lcs[m][n]
        precision = lcs_length / n if n > 0 else 0
        recall = lcs_length / m if m > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        return Score(**{'precision': precision, 'recall': recall, 'fmeasure': f1})

    def score(self, y_true, y_pred):
        return {
            'rouge1': self.rouge1(y_true, y_pred),
            'rouge2': self.rouge2(y_true, y_pred),
            'rougeL': self.rougeL(y_true, y_pred)
        }

# class Evaluator:
#     def __init__(self):
#         self.rouge = CustomRouge()
    
#     def evaluate(self, y_true:list[str], y_pred:list[str]):
#         em = exact_match(y_true, y_pred)
#         rouge1_scores = self.rouge.rouge1(y_true, y_pred)
#         rouge2_scores = self.rouge.rouge2(y_true, y_pred)
#         rougeL_scores = self.rouge.rougeL(y_true, y_pred)
        
#         return {
#             'exact_match': em,
#             'rouge1': rouge1_scores,
#             'rouge2': rouge2_scores,
#             'rougeL': rougeL_scores
#         }