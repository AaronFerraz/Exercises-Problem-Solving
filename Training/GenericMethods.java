public class GenericMethods {
    
    // a) Método para contar elementos iguais ao parâmetro
    public static <T> int countIguais(T[] vetor, T elemento) {
        int count = 0;

        for (T element : vetor){
            if(element.equals(elemento) && element != null){
                count++;
            }
        }

        return count;
    }
    
    // b) Método para contar elementos menores que o parâmetro
    public static <T extends Comparable<T>> int countMenores(T[] vetor, T elemento) { 
        int count = 0;

        for(T element : vetor){
            if(element.compareTo(elemento) == -1 && element != null){
                count++;
            }
        }

        return count;
    }
    
    public static void main(String[] args) {
        // Teste com Integer
        Integer[] numeros = {1, 3, 5, 3, 7, 3, 9};
        int alvo = 3;
        
        System.out.println("Quantidade de elementos iguais a " + alvo + ": " + 
            countIguais(numeros, alvo)); // Deve retornar 3
        
        System.out.println("Quantidade de elementos menores que " + alvo + ": " + 
            countMenores(numeros, alvo)); // Deve retornar 1 (apenas o 1)

        // Teste com String
        String[] palavras = {"apple", "banana", "apple", "cherry", "date"};
        String alvoStr = "apple";
        
        System.out.println("Quantidade de elementos iguais a '" + alvoStr + "': " + 
            countIguais(palavras, alvoStr)); // Deve retornar 2
        
        System.out.println("Quantidade de elementos menores que '" + alvoStr + "': " + 
            countMenores(palavras, alvoStr)); // Deve retornar 0 
    }
}
