### Preview the diagram

* Open your Markdown file.
* Press Cmd+Shift+V to open the Markdown preview. You should see the rendered Mermaid diagram.
* You can also use the command palette (Cmd+Shift+P) and search for "Markdown: Open Preview to the Side".


```mermaid
erDiagram

    %% === USER SERVICE ===
    User {
        int id PK
        string username
        string email
        string password
        string full_name
        string bio
        timestamp created_at
    }

    Follow {
        int follower_id FK
        int following_id FK
        timestamp created_at
    }

    Notification {
        int id PK
        int user_id FK
        string type
        int reference_id
        boolean seen
        timestamp created_at
    }

    User ||--o{ Follow : "follows"
    User ||--o{ Notification : "receives"


    %% === POST SERVICE ===
    Post {
        int id PK
        int user_id FK
        string caption
        timestamp created_at
    }

    Media {
        int id PK
        int post_id FK
        string url
        string media_type
        timestamp created_at
    }

    Comment {
        int id PK
        int post_id FK
        int user_id FK
        string text
        timestamp created_at
    }

    Like {
        int id PK
        int user_id FK
        int post_id FK
        int comment_id FK
        timestamp created_at
    }

    Post ||--o{ Media : "has"
    Post ||--o{ Comment : "receives"
    Post ||--o{ Like : "receives"
    Comment ||--o{ Like : "receives"
    User ||--o{ Post : "creates"
    User ||--o{ Comment : "writes"
    User ||--o{ Like : "reacts"


    %% === AI / GENAI SERVICE ===
    AIModeration {
        int id PK
        int post_id FK
        int comment_id FK
        string status
        string reason
        timestamp created_at
    }

    VectorEmbedding {
        int id PK
        string entity_type
        int entity_id
        vector embedding
    }

    Post ||--o{ AIModeration : "moderated"
    Comment ||--o{ AIModeration : "moderated"
    Post ||--o{ VectorEmbedding : "indexed"
    Comment ||--o{ VectorEmbedding : "indexed"

```