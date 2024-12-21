import java.rmi.*;
import java.rmi.server.*;
public class Adder extends UnicastRemoteObject implements AddServerInterface {
    public Adder() throws RemoteException{
        super();
    }
        public int sum(int a,int b) throws RemoteException{
        return a+b;
    }
}