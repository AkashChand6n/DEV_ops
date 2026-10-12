# Backend

Backend services, APIs, and business logic.

## Structure

- `src/` - Source code
  - `api/` - API endpoints
  - `services/` - Business logic
  - `models/` - Data models
  - `middleware/` - Request middleware
  - `utils/` - Utility functions
- `tests/` - Test files
- `migrations/` - Database migrations
- `config/` - Configuration files

## Development

```bash
npm install
npm run dev
```

## Testing

```bash
npm test
npm run lint
```

## Database

```bash
npm run migrate
npm run seed
```

## Standards

- Follow the coding standards defined in CLAUDE.md
- Run tests before creating PR
- Use TypeScript for type safety
- Implement proper error handling
- Use logging for debugging
- Document all API endpoints

## Security

- Never commit secrets or API keys
- Use environment variables for sensitive data
- Implement authentication and authorization
- Validate all input
- Use HTTPS in production
- Keep dependencies updated
- Implement rate limiting
- Follow OWASP guidelines

## API Documentation

Document all endpoints with:
- Request format
- Response format
- Authentication requirements
- Error responses
- Example usage
