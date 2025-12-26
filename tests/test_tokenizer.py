import pytest
from skills.evaluation.eval import CustomRouge
from rouge_score import rouge_scorer

def test_custom_rouge():
    cr = CustomRouge()
    reference = "The cat sat on the mat."
    candidate = "The cat is on mat."
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=False)

    true_score = scorer.score(reference, candidate)
    generated_score = cr.score(reference.split(), candidate.split())
    
    def assert_scores(true_s, gen_s):
        assert round(true_s.precision, 4) == round(gen_s.precision, 4)
        assert round(true_s.recall, 4) == round(gen_s.recall, 4)
        assert round(true_s.fmeasure, 4) == round(gen_s.fmeasure, 4)

    for metric in ['rouge1', 'rouge2', 'rougeL']:
        assert_scores(true_score[metric], generated_score[metric])
