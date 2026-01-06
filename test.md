erDiagram

users {
  uuid id PK
  varchar email
  varchar password_hash
  varchar display_name
  varchar bio
  uuid avatar_asset_id FK
  uuid cover_asset_id FK
  timestamptz email_verified_at
  boolean is_private
  user_status status
  uuid current_plan_id FK
  integer used_photos
  integer used_trips
  timestamptz last_login_at
  timestamptz created_at
  timestamptz updated_at
  timestamptz deleted_at
}

user_settings {
  uuid user_id PK, FK
  boolean notify_follow
  boolean notify_comment
  boolean notify_like
  boolean notify_trip
  timestamptz created_at
  timestamptz updated_at
}

user_security {
  uuid user_id PK, FK
  boolean two_factor_enabled
  varchar two_factor_method
  varchar two_factor_secret
  varchar phone_number
  timestamptz created_at
  timestamptz updated_at
}

auth_identities {
  uuid id PK
  uuid user_id FK
  varchar provider
  varchar provider_user_id
  varchar email
  varchar profile_name
  varchar avatar_url
  timestamptz connected_at
}

refresh_tokens {
  uuid id PK
  uuid user_id FK
  varchar token_hash
  timestamptz expires_at
  timestamptz revoked_at
  timestamptz last_used_at
  timestamptz created_at
}

verification_tokens {
  uuid id PK
  uuid user_id FK
  varchar email
  verification_purpose purpose
  varchar token
  verification_status status
  timestamptz expires_at
  timestamptz used_at
  timestamptz created_at
}

device_tokens {
  uuid id PK
  uuid user_id FK
  device_platform platform
  varchar token
  varchar device_id
  varchar app_version
  timestamptz last_seen_at
  timestamptz revoked_at
}

search_histories {
  uuid id PK
  uuid user_id FK
  search_type search_type
  varchar query
  timestamptz created_at
}

follows {
  uuid id PK
  uuid follower_id FK
  uuid following_id FK
  follow_status status
  timestamptz created_at
}

notifications {
  uuid id PK
  uuid user_id FK
  uuid actor_id FK
  notification_type type
  notification_status status
  timestamptz read_at
  timestamptz created_at
}

notification_targets {
  uuid id PK
  uuid notification_id FK
  notification_target_type target_type
  uuid target_id
}

plans {
  uuid id PK
  varchar code
  varchar name
  integer price_amount
  char price_currency
  varchar billing_interval
  integer max_photos
  integer max_trips
}

subscriptions {
  uuid id PK
  uuid user_id FK
  uuid plan_id FK
  subscription_status status
  timestamptz current_period_start
  timestamptz current_period_end
}

payments {
  uuid id PK
  uuid user_id FK
  uuid subscription_id FK
  integer amount
  payment_status status
  timestamptz paid_at
}

assets {
  uuid id PK
  uuid user_id FK
  upload_purpose purpose
  varchar asset_key
  varchar mime_type
  bigint size_bytes
}

trips {
  uuid id PK
  uuid user_id FK
  varchar title
  trip_category category
  timestamptz started_at
  timestamptz ended_at
}

trip_categories {
  uuid id PK
  uuid user_id FK
  varchar name
  integer color
}

places {
  uuid id PK
  place_provider provider
  varchar provider_place_id
  varchar name
  double lat
  double lng
}

pins {
  uuid id PK
  uuid trip_id FK
  uuid place_id FK
  boolean is_active
}

media {
  uuid id PK
  uuid pin_id FK
  media_type type
  timestamptz taken_at
  boolean is_favorite
}

media_files {
  uuid id PK
  uuid media_id FK
  uuid asset_id FK
  media_file_role role
}

media_comments {
  uuid id PK
  uuid media_id FK
  uuid user_id FK
  uuid parent_id
  varchar content
}

media_likes {
  uuid id PK
  uuid media_id FK
  uuid user_id FK
}

trip_routes {
  uuid id PK
  uuid trip_id FK
  route_source source
}

trip_shares {
  uuid id PK
  uuid trip_id FK
  uuid created_by FK
  varchar token
}

trip_exports {
  uuid id PK
  uuid trip_id FK
  uuid requested_by FK
  export_type type
  export_status status
}

%% Relationships
users ||--|| user_settings : has
users ||--|| user_security : has
users ||--o{ auth_identities : connects
users ||--o{ refresh_tokens : owns
users ||--o{ device_tokens : uses
users ||--o{ search_histories : searches
users ||--o{ follows : follows
users ||--o{ notifications : receives
users ||--o{ trips : creates
users ||--o{ assets : uploads
users ||--o{ subscriptions : subscribes
users ||--o{ payments : pays

plans ||--o{ subscriptions : includes

trips ||--o{ pins : has
trips ||--o{ trip_routes : has
trips ||--o{ trip_shares : shares
trips ||--o{ trip_exports : exports

pins ||--o{ media : contains
media ||--o{ media_files : stores
media ||--o{ media_comments : commented
media ||--o{ media_likes : liked

places ||--o{ pins : mapped
