package training.algorithmsjava;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class SlidingWindow{

    /**
     * O Problema Clássico: Maior Substring Sem Caracteres Repetidos
     * 
     * Usos
     * HashSet - evitar duplicações e principalmente por ssa estrutura oferecer operações extremamente eficientes sendo O(1), na verificação, inserção e remoção.
     * right: ponteiro da direita da janela
     * left: ponteiro da esquerda da janela
     * 
     * A janela desliza se encontrar um caractere presente no "set". Caso contrário, adiciona na estrutura.
     * Cada caractere é adicionado no máximo uma vez na janela e removido no máximo uma vez.
     * tamanho atual da janela = right - left + 1 (quantos caracteres tenho entre left e right)
     * 
     * Complexidade do Algoritmo: O(n)
     */

    public static int lengthOfLongestSubstring(String st){
        Set<Character> windowString = new HashSet<>();
        int left = 0, maxLength = 0;

        for(int right = 0; right < st.length(); right++){
            while(windowString.contains(st.charAt(right))){
                windowString.remove(st.charAt(left));
                left++;
            }

            windowString.add(st.charAt(right));
            maxLength = Math.max(maxLength, right-left+1);
        }

        return maxLength;
    }


    public static int Solucao2(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }

        // caractere:indice
        Map<Character, Integer> mapIndices = new HashMap<>();
        int maxLength = 0, left = 0; 

        for (int right = 0; right < s.length(); right++) {
            char charAtual = s.charAt(right);

            // Se o caractere já foi visto E sua última posição está DENTRO da janela atual
            if (mapIndices.containsKey(charAtual) && mapIndices.get(charAtual) >= left) {
                left = mapIndices.get(charAtual) + 1;
            }

            // Atualiza o mapa com a posição mais recente do caractere atual
            mapIndices.put(charAtual, right);

            // Calcula o comprimento da janela atual e atualiza o máximo se necessário
            int comprimentoAtual = right - left + 1;
            maxLength = Math.max(maxLength, comprimentoAtual);
        }

        return maxLength;
    }

    
    public static void main(String[] args) {
        //Teste 1
        String input = "abcabcbb";
        System.out.println("Maior substring sem repetir: " + lengthOfLongestSubstring(input)); // Output esperado: 3
        
        System.out.println("Maior substring sem repetir: " + Solucao2(input)); // Esperado: 3

        //Teste 2
        String input2 = "";
        System.out.println("Maior substring sem repetir: " + lengthOfLongestSubstring(input2)); // Output esperado:: 0
        
        //Teste 3
        String input3 = "bbbbb";
        System.out.println("Maior substring sem repetir: " + lengthOfLongestSubstring(input3)); // Output esperado:: 1
        
        
        //Teste 4
        String input4 = "pwwkewqs";
        System.out.println("Maior substring sem repetir: " + lengthOfLongestSubstring(input4)); // Output esperado: 5
        
        
        //Teste 5
        String input5 = "aabcdefghbb";
        System.out.println("Maior substring sem repetir: " + lengthOfLongestSubstring(input5)); // Output esperado: 8
        
    }
}


/*
Passo a Passo do primeiro teste:
Iteração 0: [a] b c a b c b b
Iteração 1: [a b] c a b c b b
Iteração 2: [a b c] a b c b b   <- maxLength=3
Iteração 3: a [b c a] b c b b   <- Janela desliza
Iteração 4: a b [c a b] c b b   <- Janela desliza
Iteração 5: a b c [a b c] b b   -> Contém 'b' repetido? Vamos deslizar...
Iteração 6: a b c a [b c] b b   -> Janela desliza para remover 'b' repetido
Iteração 7: a b c a b [c b] b   
Iteração 6: a b c a b c [b] b 
Iteração 8: a b c a b c b [b] 
 */