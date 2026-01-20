// S3_PIPE_05 — Log lines pipeline

const pipe =
  (...fns) =>
  (value) =>
    fns.reduce((acc, fn) => fn(acc), value);

// Step 1: parse lines into objects
const parse = (lines) =>
  lines.map((line) => {
    const [level, rest] = line.split(": ");
    const [, user] = rest.split("=");
    return { level, userId: Number(user) };
  });

// Step 2: keep only INFO logs
const onlyInfo = (logs) => logs.filter((log) => log.level === "INFO");

// Step 3: extract user ids
const extractUserIds = (logs) => logs.map((log) => log.userId);

// Build pipeline
const getInfoUserIds = pipe(parse, onlyInfo, extractUserIds);

// Tests
const lines = ["INFO: user=42", "ERROR: user=7", "INFO: user=13"];

console.log(getInfoUserIds(lines)); // [42, 13]
