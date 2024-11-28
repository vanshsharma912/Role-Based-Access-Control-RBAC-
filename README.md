# Role-Based-Access-Control-RBAC
The goal of this assignment is to assess your understanding and implementation skills regarding Authentication, Authorization, and Role-Based Access Control (RBAC).

# Features <br>
<li>User Registration, Login, and Logout.<br>
<li>Role-Based Access Control (RBAC) with roles:</li>
<ul><li>Admin: Full access to all endpoints.</li><br>
<li>Moderator: Limited access to specific resources.</li><br>
<li>User: Basic access permissions.</li></ul>
<li>Secure Authentication using JWT (JSON Web Tokens).</li> <br>
<li>Endpoints protected with role-specific permissions.</li>

# Technologies_Used <br>
<li>Django: Web framework.</li><br>
<li>Django REST Framework: API development.</li><br>
<li>SimpleJWT: JWT-based authentication.</li><br>
<li>SQLite: Default database (can be swapped for other databases).</li>

# Endpoints
# Authentication
<li>Register: POST /api/users/register/</li>
<li>Login (Obtain JWT): POST /api/token/</li>
<li>Refresh Token: POST /api/token/refresh/</li>
# Role-Based Access
<li>Admin-only Endpoint: GET /api/users/admin-only/ (Requires Admin role)</li>
<li>Moderator-only Endpoint: GET /api/users/moderator-only/ (Requires Moderator role)</li>
