package notes;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import static org.assertj.core.api.Assertions.assertThat;
@DataJpaTest
class JpaArticleQueriesTest {
 @Autowired TaskRepository repository;
 @Test void derivedJpqlAndNativeQueries() {
  repository.saveAndFlush(new Task("Vue 練習"));
  repository.saveAndFlush(new Task("Java 練習"));
  assertThat(repository.findByTitleStartingWithOrderByIdAsc("Vue")).hasSize(1);
  assertThat(repository.findExact("Vue 練習")).hasSize(1);
  assertThat(repository.findExactNative("Vue 練習")).hasSize(1);
  assertThat(repository.findExact("missing")).isEmpty();
 }
}
