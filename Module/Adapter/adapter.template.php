<?php

/**
 * Camada de Acesso ao Banco de Dados
 * @author Víctor Vaz <victor@operacaosistemas.com.br>
 */
class Adapter
{
    /**
     * Servidor
     * @var String
     */
    private static $SERVIDOR = "{%__SERVIDOR__%}";

    /**
     * Usuário do banco de dados
     * @var String
     */
    private static $USUARIO = "{%__USUARIO__%}";
    
    /**
     * Senha correspondente ao usuário do banco de dados.
     * @var String
     */
    private static $SENHA = "{%__SENHA__%}";
    
    /**
     * Banco de dados
     * @var String
     */
    private static $BANCO = "{%__BANCO__%}";
    
    /**
     * Conexão com o banco de dados.
     * @var mysqli_connection 
     */
    private static $conexao;

    /**
     * Método para conectar com o banco de dados.
     * @return Connection
     * @throws SQLConnectionLostException
     */
    private static function conectar() {
        if (Adapter::$conexao)
            return Adapter::$conexao;
        
        Adapter::$conexao = mysqli_connect(Adapter::$SERVIDOR, Adapter::$USUARIO, Adapter::$SENHA, Adapter::$BANCO)
                or die ("Não foi possível estabelecer uma conexão com o banco de dados.");
        
        return Adapter::$conexao;
    }
    
    /**
     * Método para executar uma query no banco de dados
     * @param String $sql
     * @return Result
     * @throws SQLCommandException
     */
    public static function query($sql) {
        $query = mysqli_query(Adapter::conectar(), $sql)
                or die("Não foi possível executar um comando ao banco de dados." . mysqli_error(Adapter::$conexao));
        
        return $query;
    }
}
?>