import java.rmi.*;
import java.rmi.registry.*;

public class AddServer {
    public static void main(String args[]) {
        try {
            // Cria o objeto do serviço
            AddServerInterface addService = new Adder();

            // Inicia o RMI Registry (se não estiver em execução) ou apenas obtém a referência
            LocateRegistry.createRegistry(1099);

            // Registra o serviço no RMI Registry com o nome "AddService"
            Naming.rebind("rmi://127.0.0.1/AddService", addService);

            System.out.println("Servidor RMI está pronto.");
        } catch (Exception e) {
            System.out.println("Erro: " + e);
        }
    }
}
