package training.algorithmsjava;

public class SortingAlgorithms {

    public static void quickSort(int[] v, int left, int right){
        /*
            Escolha um pivô
            Separe os elementos menores que o pivô para a esquerda
            e os elementos maiores que o pivô para direita.
            Recursivamente, execute o mesmo procedimento para elementos à esquerda do pivô
            Recursivamente, execute o mesmo procedimento para elementos à direita do pivô

            Defina i e j começando pela esquerda e direita respectivamente.
            Faça uma varredura com a variável i para a direita até que encontre um elemento v[i] maior que o pivô
            Faça uma varredura com a variável j para a esquerda até que encontre um elemento v[j] menor que o pivô
            troque v[i] com v[j]
        */
        
            if(left < right){
                int j = separate(v, left, right);
                quickSort(v, left, j-1);
                quickSort(v, j+1, right);
            }
    }

    private static int separate(int[] v, int left, int right){
        int i = left + 1;
        int j = right;
        int pivot = v[left];

        while (i <= j){
            if (v[i] <= pivot) i++;
            else if (v[j] > pivot) j--;
            else if (i <= j){
                swap(v, i, j);
                i++;
                j--;
            }
        }

        swap(v, left, j);
        return j;
    }

    private static void swap(int[] v, int i, int j){
        int aux = v[i];
        v[i] = v[j];
        v[j] = aux;
    }

    private static int[] generateRandomArray(int size, int maxValue){
        int[] v = new int[size];
        for (int i = 0; i < size; i++) {
            v[i] = (int)(Math.random() * maxValue);
        }
        return v;
    }


    public static void main(String[] args) {
        // Quicksort

        int n = 10;
        for(int i = 0; i < n; i++){
            int[] v = generateRandomArray(8, 15);
            quickSort(v, 0, v.length-1);
            System.out.println("Vetor ordenado com Quicksort:" + java.util.Arrays.toString(v));
        }
    }
}
