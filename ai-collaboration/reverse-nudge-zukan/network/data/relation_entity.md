```mermaid
erDiagram
    CHARACTERS {
        string id
        string name
        string emoji
        string title
        string origin_period
        string category
        string affiliation
        string traits
        string signature_line
        string nemesis
        string notes
        string image_prompt
        string scene_prompt
        string role_level
    }

    RELATIONS {
        string source_id
        string target_id
        string relation_type
        string description
    }

    CHARACTERS ||--o{ RELATIONS : has_source
    CHARACTERS ||--o{ RELATIONS : has_target

```
