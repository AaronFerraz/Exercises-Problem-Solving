package training.algorithmsjava;

import java.util.stream.IntStream;

public class Exercises {
    /* 
        Se listarmos os números naturais abaixo de 10 que são múltiplos
        de 3 ou 5, obtemos 3, 5, 6 e 9. A soma destes números é 23.
        Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000. 
    */
        public static void LambdaExercise(){
            int sum = IntStream.range(1, 1000)
                .filter(n -> n % 3 == 0 || n % 5 == 0)
                .sum();
            System.out.println("Soma dos múltiplos de 3 ou 5 abaixo de 1000: " + sum);
        }

    /*
        Deseja-se ir da esquina A para a esquina B no mapa abaixo. As ruas são todas de mão
        única como indicado pelas flechas.
        Escreva um método que determine de quantas maneiras é possível executar o trajeto
    */
    public static int countWays(int m, int n){
        // m - altura
        // n - comprimento
        if(m == 0 || n == 0){ // um único caminho
            return 1;
        } else {
            return countWays(m-1, n) + countWays(m, n-1);
        }
    }


    public static void main(String[] args) {
        LambdaExercise();

        System.out.println("Número de maneiras de ir da esquina A para a esquina B: " + countWays(5, 7));
    }
}
