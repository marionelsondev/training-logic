package TiposDeDados;

public class DadosNaoPrimitivos {
    public static void main(String[] args) {
        String nome = "Naruto Uzumaki";
        String aldeia = "Aldeia da Folha";

        String nomeUpperCase = nome.toUpperCase();
        String aldeiaLowerCase = aldeia.toLowerCase();

        System.out.println("Nome em UPPER: " + nomeUpperCase);
        System.out.println("Aldeia em LOWER: " + aldeiaLowerCase);
    }
}
