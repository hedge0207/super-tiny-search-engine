import pytest
from unittest.mock import patch, MagicMock

from core.tokenizer.korean import KoreanTokenizer


class TestKoreanTokenizer:
    def test_clean_text(self):
        tokenizer = KoreanTokenizer()
        assert tokenizer._clean_text("Hello! World?") == "Hello World"
        assert tokenizer._clean_text("안녕하세요! 반갑습니다.") == "안녕하세요 반갑습니다"
        assert tokenizer._clean_text("123!@#") == "123"
    
    @patch('mecab.MeCab')
    def test_tokenize(self, mock_mecab_class):
        # MeCab 인스턴스 모의 객체 생성
        mock_mecab = MagicMock()
        mock_mecab.morphs.return_value = ["안녕하세요", "반갑습니다"]
        mock_mecab_class.return_value = mock_mecab
        
        # KoreanTokenizer 인스턴스 생성
        tokenizer = KoreanTokenizer()
        
        # tokenize 메서드 호출
        result = tokenizer.tokenize("안녕하세요! 반갑습니다.")
        
        # 결과 검증
        assert result == ["안녕하세요", "반갑습니다"]
        mock_mecab.morphs.assert_called_once_with("안녕하세요 반갑습니다") 