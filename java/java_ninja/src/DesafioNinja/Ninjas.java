package DesafioNinja;

public class Ninjas {
    public static void main(String[] args) {
        // Ninja 1

        String nomeNinja1 = "Naruto Uzumaki";
        int idadeNinja1 = 15;
        String missaoNinja1 = "Proteger o construtor de pontes Tazuna até o País das Ondas";
        char nivelMissaoNinja1 = 'C';
        String statusMissaoNinja1 = "não concluída";

        // Ninja 2

        String nomeNinja2 = "Sasuke Uchiha";
        int idadeNinja2 = 12;
        String missaoNinja2 = "Investigar rumores sobre Itachi na Vila da Névoa";
        char nivelMissaoNinja2 = 'B';
        String statusMissaoNinja2 = "não concluída";

        // Ninja 3

        String nomeNinja3 = "Kakashi Hatake";
        int idadeNinja3 = 29;
        String missaoNinja3 = "Interceptar espiões da Vila do Som";
        char nivelMissaoNinja3 = 'B';
        String statusMissaoNinja3 = "não concluída";

        if (idadeNinja1 >= 15 || nivelMissaoNinja1 == 'C' || nivelMissaoNinja1 == 'D') {
            statusMissaoNinja1 = "concluída";
        }

        if (idadeNinja2 >= 15 || nivelMissaoNinja2 == 'C' || nivelMissaoNinja2 == 'D') {
            statusMissaoNinja2 = "concluída";
        }

        if (idadeNinja3 >= 15 || nivelMissaoNinja3 == 'C' || nivelMissaoNinja3 == 'D') {
            statusMissaoNinja3 = "concluída";
        }

        System.out.println();
        System.out.println("====== Ninja 1 ======");
        System.out.println("Nome - " + nomeNinja1);
        System.out.println("Idade - " + idadeNinja1);
        System.out.println("Missão - " + missaoNinja1);
        System.out.println("Nível da missão - " + nivelMissaoNinja1);
        System.out.println("Status da missão - " + statusMissaoNinja1);
        System.out.println();

        System.out.println("====== Ninja 2 ======");
        System.out.println("Nome - " + nomeNinja2);
        System.out.println("Idade - " + idadeNinja2);
        System.out.println("Missão - " + missaoNinja2);
        System.out.println("Nível da missão - " + nivelMissaoNinja2);
        System.out.println("Status da missão - " + statusMissaoNinja2);
        System.out.println();

        System.out.println("====== Ninja 3 ======");
        System.out.println("Nome - " + nomeNinja3);
        System.out.println("Idade - " + idadeNinja3);
        System.out.println("Missão - " + missaoNinja3);
        System.out.println("Nível da missão - " + nivelMissaoNinja3);
        System.out.println("Status da missão - " + statusMissaoNinja3);

    }
}
