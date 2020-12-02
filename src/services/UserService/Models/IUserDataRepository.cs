using MySql.Data;
using MySql.Data.MySqlClient;

namespace User
{
    public interface IUserDataRepository
    {
        public MySqlConnection GetConnection();
    }
}