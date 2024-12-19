import java.rmi.*;
public interface AddServerInterface extends Remote{
        int sum(int a,int b) throws RemoteException;
}
